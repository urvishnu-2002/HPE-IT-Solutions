from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient, ReturnDocument
from flasgger import Swagger
from datetime import datetime

app = Flask(__name__, template_folder='.')
CORS(app)
swagger = Swagger(app)

# ==============================
# MONGODB CONNECTION
# ==============================
MONGO_URI = "mongodb+srv://urvishnu:urvishnu1546@mydbcluster.kczb8ak.mongodb.net/?appName=MyDbCluster"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["HPE_DB"]
    contacts_col = db["contactinfo"]
    counters_col = db["counters"]  # To manage auto-incrementing IDs
    print("✅ MongoDB connection initialized")
except Exception as e:
    print(f"⚠️ MongoDB connection failed: {e}")
    # Create dummy collections to prevent crashes
    db = None
    contacts_col = None
    counters_col = None

def get_next_sequence(name):
    """Generates a simple integer ID (1, 2, 3...)"""
    if counters_col is None:
        print("⚠️ Database not available, using fallback ID")
        return 1

    count_doc = counters_col.find_one_and_update(
        {"_id": name},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    return count_doc["seq"]

def initialize_db():
    if db is None:
        print("⚠️ Database not available")
        return

    try:
        client.admin.command('ping')
        print("✅ MongoDB Atlas Connected & Initialized")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

initialize_db()

# ==============================
# CONTACT ROUTES
# ==============================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/contacts/all", methods=["GET"])
def get_all_contacts():
    """
    Get all contacts
    ---
    tags:
      - Contacts
    responses:
      200:
        description: A list of contacts
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
              phone:
                type: string
              category:
                type: string
              description:
                type: string
              status:
                type: string
              timestamp:
                type: string
    """
    contacts = list(contacts_col.find().sort("cid", -1)) # Newest first
    output = []
    for c in contacts:
        output.append({
            "id": c.get("cid"), # Using our custom simple integer ID
            "name": c.get("contactname"),
            "email": c.get("contactmail"),
            "phone": c.get("contactno"),
            "category": c.get("contactcategory"),
            "description": c.get("contactdescription"),
            "status": c.get("status", "new"),
            "timestamp": c.get("timestamp", datetime.now().isoformat())
        })
    return jsonify(output), 200

@app.route("/api/contact/save", methods=["POST"])
def contact_form():
    """
    Save a new contact
    ---
    tags:
      - Contacts
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
            - phone
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
            category:
              type: string
            description:
              type: string
    responses:
      200:
        description: Contact saved successfully
      409:
        description: Email or Phone already exists
      500:
        description: Internal server error
    """
    data = request.json
    email = data.get("email")
    phone = data.get("phone")

    # Check for Unique Email or Phone
    existing = contacts_col.find_one({
        "$or": [
            {"contactmail": email},
            {"contactno": phone}
        ]
    })

    if existing:
        return jsonify({"error": "Email or Phone Number already exists. Please use another one."}), 409

    try:
        contacts_col.insert_one({
            "cid": get_next_sequence("contact_id"), # Auto-incrementing 1, 2, 3...
            "contactname": data.get("name"),
            "contactmail": email,
            "contactno": phone,
            "contactcategory": data.get("category"),
            "contactdescription": data.get("description"),
            "status": "new",
            "timestamp": datetime.now().isoformat()
        })
        return jsonify({"message": "✅ Message Sent Successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/contact/delete/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    """
    Delete a contact
    ---
    tags:
      - Contacts
    parameters:
      - name: contact_id
        in: path
        type: integer
        required: true
        description: ID of the contact to delete
    responses:
      200:
        description: Contact deleted successfully
      404:
        description: Record not found
    """
    # Now we just filter by the simple integer 'cid'
    result = contacts_col.delete_one({"cid": contact_id})
    if result.deleted_count > 0:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Record not found"}), 404

@app.route("/api/contact/status/<int:contact_id>", methods=["PATCH"])
def update_contact_status(contact_id):
    """
    Update contact status
    ---
    tags:
      - Contacts
    parameters:
      - name: contact_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            status:
              type: string
    responses:
      200:
        description: Status updated successfully
    """
    data = request.json
    new_status = data.get("status")
    
    result = contacts_col.update_one(
        {"cid": contact_id},
        {"$set": {"status": new_status}}
    )
    
    if result.modified_count > 0 or result.matched_count > 0:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Record not found"}), 404

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)