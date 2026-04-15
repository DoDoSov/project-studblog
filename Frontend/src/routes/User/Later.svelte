<script>
  // Sample data for saved posts
  let savedPosts = $state([
    { id: 101, title: "How I Fixed My Sleep During Exam Season", author: "Elena L.", time: "7 min read", icon: "🌙" },
    { id: 102, title: "Student Investing 101: €200 → €1,400", author: "Lukas P.", time: "11 min read", icon: "📈" }
  ]);

  function removeSaved(id) {
    savedPosts = savedPosts.filter(p => p.id !== id);
  }
</script>

<div class="h-32"></div>
<section class="max-w-5xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  <div class="mb-10 flex items-center justify-between">
    <div>
      <p class="text-[10px] font-black text-blue-400 tracking-widest uppercase mb-2">Your Library</p>
      <h1 class="text-4xl font-bold text-white">Saved for Later</h1>
    </div>
    <div class="bg-blue-500/10 border border-blue-500/20 px-4 py-2 rounded-xl">
      <span class="text-blue-400 font-bold">{savedPosts.length} Articles</span>
    </div>
  </div>

  <div class="grid gap-4">
    {#each savedPosts as post}
      <div class="bg-[#1A1F2E] p-6 rounded-[2rem] border border-white/5 flex items-center justify-between hover:border-white/20 transition-all group">
        <div class="flex items-center gap-5">
          <div class="size-12 bg-white/5 rounded-2xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">
            {post.icon}
          </div>
          <div>
            <h3 class="text-white font-bold mb-1">{post.title}</h3>
            <p class="text-[10px] text-gray-500 uppercase font-medium">{post.author} • {post.time}</p>
          </div>
        </div>
        <button 
          onclick={() => removeSaved(post.id)}
          class="text-gray-500 hover:text-red-400 text-xs font-bold uppercase tracking-widest transition-colors p-2"
        >
          Remove
        </button>
      </div>
    {:else}
      <div class="bg-[#1A1F2E] p-20 rounded-[3rem] border border-white/5 text-center">
        <p class="text-gray-500 font-bold italic">Your reading list is empty.</p>
      </div>
    {/each}
  </div>
</section>