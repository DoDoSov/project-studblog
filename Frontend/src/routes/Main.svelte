<script>
  import Category from '../lib/components/Category.svelte';
  import PostCard from '../lib/components/PostCard.svelte';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import Promo from '../lib/components/Promo.svelte';

  // Receive the navigation function from App.svelte
  let { onPostClick } = $props();

  let selectedCategory = $state("Technology");

  const allPosts = [
    { title: "Getting Started with JavaScript in 2026", description: "A beginner-friendly ...", image: "https://picsum.photos/seed/js/600/400", tags: ["JavaScript", "WebDev"], category: "Technology", type: "trending" },
    { title: "Student Investing 101: €200 → €1,400", description: "Consistent ETF investing...", author: "Lukas P.", initials: "LP", likes: 203, category: "Finance", type: "small" },
    { title: "The Future of AI in Web Design", description: "How generative tools...", image: "https://picsum.photos/seed/ai-web/600/400", tags: ["AI", "Design"], category: "AI", type: "latest" },
    { title: "How I Fixed My Sleep During Exams", description: "Science-backed protocol...", author: "Elena L.", initials: "EL", likes: 315, category: "Health", type: "small" },
    { title: "Mastering Tailwind v4", description: "Everything you need...", image: "https://picsum.photos/seed/tailwind/600/400", tags: ["CSS", "Tailwind"], category: "Technology", type: "latest" },
    { title: "CRISPR in 2026", description: "Student Labs Join Gene Editing...", author: "Maria K.", initials: "MK", likes: 89, category: "Science", type: "small" }
  ];

  let trendingPosts = $derived(allPosts.filter(p => p.type === "trending" && (selectedCategory === "All" || p.category === selectedCategory)));
  let latestPosts = $derived(allPosts.filter(p => p.type === "latest" && (selectedCategory === "All" || p.category === selectedCategory)));
  let morePosts = $derived(allPosts.filter(p => p.type === "small" && (selectedCategory === "All" || p.category === selectedCategory)));

  function handleCategoryChange(category) {
    selectedCategory = category;
  }
</script>

<div class="h-32"></div>

<div class="bg-[#283047] rounded-2xl max-w-7xl mx-auto px-4 md:px-6 flex flex-col gap-12 pb-20 text-white font-sans">
  <div class="h-4"></div>
  <Category onSelect={handleCategoryChange} />

  <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl transition-all duration-500">
    <div class="flex items-center gap-4 mb-8">
      <h2 class="text-sm font-black text-blue-400 uppercase tracking-widest">Trending</h2>
      <div class="h-[1px] flex-grow bg-white/5"></div>
      <span class="text-[10px] font-bold text-gray-500 uppercase">{selectedCategory}</span>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each trendingPosts as post}
      <PostCard 
        {...post} 
        onRead={() => onPostClick(post)} 
      />
      {:else}
        <p class="col-span-full text-center py-10 text-gray-500 italic">No trending posts in {selectedCategory} yet.</p>
      {/each}
    </div>
  </section>

  <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl transition-all duration-500">
    <div class="flex items-center gap-4 mb-8">
      <h2 class="text-sm font-black text-purple-400 uppercase tracking-widest">Latest</h2>
      <div class="h-[1px] flex-grow bg-white/5"></div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each latestPosts as post}
        <PostCard {...post} onRead={() => onPostClick(post)} />
      {:else}
        <p class="col-span-full text-center py-10 text-gray-500 italic">No new posts in this category.</p>
      {/each}
    </div>
  </section>

  <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl transition-all duration-500">
    <div class="flex items-center gap-4 mb-8">
      <h2 class="text-sm font-black text-green-400 uppercase tracking-widest">Discovery</h2>
      <div class="h-[1px] flex-grow bg-white/5"></div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {#each morePosts as post}
        <PostCardSmall {...post} />
      {:else}
        <p class="col-span-full text-center py-10 text-gray-500 italic">Keep exploring other categories!</p>
      {/each}
    </div>
  </section>

  <Promo />
</div>