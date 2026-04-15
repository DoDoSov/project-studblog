<script>
  let likedPosts = $state([
    { id: 201, title: "Mastering Tailwind v4: Everything you need to know", likes: 1420, date: "2 days ago" },
    { id: 202, title: "The Future of AI in Web Design", likes: 856, date: "1 week ago" }
  ]);
</script>

<div class="h-32"></div>
<section class="max-w-5xl mx-auto px-6 mb-20">
  <div class="mb-10">
    <p class="text-[10px] font-black text-red-400 tracking-widest uppercase mb-2">Interactions</p>
    <h1 class="text-4xl font-bold text-white">Liked Content</h1>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    {#each likedPosts as post}
      <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 relative overflow-hidden group hover:bg-white/[0.02] transition-colors">
        <div class="relative z-10">
          <div class="flex items-center gap-2 mb-4">
            <span class="text-red-500 text-lg">❤️</span>
            <span class="text-[10px] text-gray-500 font-black uppercase tracking-tighter">{post.likes} People liked this</span>
          </div>
          <h2 class="text-xl font-bold text-white mb-6 leading-tight">{post.title}</h2>
          <div class="flex justify-between items-center">
            <span class="text-[10px] text-gray-600 font-bold uppercase">{post.date}</span>
            <button class="text-[10px] font-black text-white hover:text-red-400 uppercase tracking-widest transition-colors">
              View Post →
            </button>
          </div>
        </div>
        <span class="absolute -right-4 -bottom-4 text-7xl opacity-[0.03] group-hover:scale-125 transition-transform duration-700">❤️</span>
      </div>
    {/each}
  </div>
</section>