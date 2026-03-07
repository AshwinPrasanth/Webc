url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
from webc import web

# Step 1: Load the site as a Resource
site = web[url]

# Step 2: Access the structured layer
print("=== STRUCTURE ===")
print("Title:", site.structure.title)
print("First 5 links:", site.structure.links[:5])

# Step 3: Access the query layer
print("\n=== QUERY ===")
headings = site.query["h1, h2"]
print("Headings found:")
for h in headings:
    print("-", h.get_text(strip=True))


# Step 4: Access the task layer
print("\n=== TASK ===")
summary = site.task.summarize(max_chars=1000, refine=False)
print("Summary (5000 chars):")
print(summary)

'''from webc import web

target_url = "https://openai.com/index/the-truth-elon-left-out/"
res = web[target_url]

print(f"--- 1. TITLE ---\n{res.structure.title}\n")

# Testing if our refined summary handles modern <div> layouts
print(f"--- 2. REFINED SUMMARY ---\n{res.task.summarize(max_chars=250)}\n")

# Testing the 'Dual-Mode' Metadata Miner (v0.2.1)
meta = res.structure.metadata
print(f"--- 3. DETECTED SOCIAL METADATA ---")
print(f"OG Title: {meta.get('og:title')}")
print(f"OG Description: {meta.get('og:description')}")
print(f"Twitter Image: {meta.get('twitter:image')}")

# Testing the Image Collection
images = res.structure.images
print(f"\n--- 4. IMAGE VACUUM ---")
print(f"Found {len(images)} images total.")
if images:
    print(f"Primary Image URL: {images[0]}")'''