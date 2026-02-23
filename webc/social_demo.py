from webc.websoc import social

# Target: The high-production music video
target_url = "https://www.youtube.com/watch?v=TROFVicWrTE" 

print("📺 WEBC: YOUTUBE DEEP-DATA EXTRACTION")
print("="*65)

# 1. Initialize and Fetch
print(f"📡 Fetching: {target_url}...")
view = social[target_url]

# 2. Get Video Identity
print(f"\n🎥 VIDEO TITLE: {view.preview['title']}")
print(f"🔗 VIDEO ID:    {view.video_id}")

# 3. Engagement (The working metrics)
m = view.metrics
print(f"\n📊 ENGAGEMENT METRICS:")
print(f"   • Views: {m.get('views', 'N/A')}")
print(f"   • Likes: {m.get('likes', 'N/A')}")

# 4. Full Metadata Block (Production Credits, Artists, Release Info)
# This prints the entire decoded block we captured in _extract_all
metadata = m.get('metadata')

print(f"\n📝 FULL VIDEO METADATA & CREDITS:")
print("-" * 65)

if metadata and "Enjoy the videos" not in metadata:
    # This preserves the line breaks for Director, Engineer, Lyricist etc.
    print(metadata)
else:
    # If we are still hitting the generic YouTube landing page text
    print("⚠️  Warning: Metadata blocked or generic. Check if Pattern B in extraction is active.")

print("-" * 65)
print("\n" + "="*65)