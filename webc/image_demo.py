from webc import web

site = web["https://www.audi.ie/en/"]

'''# List main images
images = site.structure.images
print(f"Found {len(images)} main content images")
print(images[:5])

# Save images safely
saved_files = site.structure.save_images(folder="audi_images1")
print(f"Saved {len(saved_files)} images locally")'''

site.structure.save_tables("audi_data")