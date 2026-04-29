<script>
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  
  // Example data
  const recommended = [
    { title: "React Performance: The 2026 Guide", category: "TECH", initials: "JS", author: "James S.", likes: 850 },
    { title: "Sustainable Living on a Student Budget", category: "LIFE", initials: "ML", author: "Maya L.", likes: 420 }
  ];
</script>

<div class="h-32"></div>

<section class=" bg-[#283047] rounded-2xl py-4 max-w-7xl mx-auto px-6 mb-20 space-y-12">
  <div class="mt-4"></div>
  <div>
    <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
      <span class="text-purple-500">★</span> Recommended for You
    </h2>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {#each recommended as post}
        <div class="bg-purple-600/5 border border-purple-500/20 p-6 rounded-[2rem] hover:bg-purple-600/10 transition-colors">
          <PostCardSmall {...post} />
        </div>
      {/each}
    </div>
  </div>

  <div class="bg-[#1A1F2E] p-8 rounded-[3rem] border border-white/5">
    <div class="flex justify-between items-center mb-8">
      <h2 class="text-xl font-bold text-white">Trending Globally</h2>
      <span class="text-xs text-gray-500 uppercase font-black tracking-widest">Live Updates</span>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="bg-white/5 h-48 rounded-2xl animate-pulse"></div>
      <div class="bg-white/5 h-48 rounded-2xl animate-pulse"></div>
      <div class="bg-white/5 h-48 rounded-2xl animate-pulse"></div>
    </div>
  </div>
  <div class="mb-4"></div>
</section>