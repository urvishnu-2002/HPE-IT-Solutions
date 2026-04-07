export default function sitemap() {
  const baseUrl =
    (process.env.NEXT_PUBLIC_BASE_URL || "https://www.hpeitsolutions.com/").replace(/\/$/, "");

  const routes = [
    "",
    "/about",
    "/vision-mission",
    "/strength",
    "/corporate-structure",
    "/services",
    "/services/enterprise",
    "/services/infrastructure",
    "/services/workforce",
    "/projects",
    "/projects/group-1",
    "/projects/group-2",
    "/projects/group-3",
    "/projects/major",
    "/projects/mid",
    "/projects/large",
    "/certifications",
    "/growth-strategy",
    "/contact",
  ];

  return routes.map((route) => ({
    url: `${baseUrl}${route}`,
    lastModified: new Date(),
    changeFrequency: "monthly",
    priority: route === "" ? 1 : 0.8,
  }));
}