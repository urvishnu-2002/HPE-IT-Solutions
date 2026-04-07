import axios from "axios";

const BASE_URL = "https://hpe-it-solutions.onrender.com";

const api = axios.create({
    baseURL: BASE_URL,
    timeout: 10000, // 10 second timeout — prevents Render cold-start from hanging the form
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;