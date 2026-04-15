<script>
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';

  const featured = {
    title: "Understanding REST APIs with Real Examples: A Student's Field Guide",
    description: "APIs are everywhere — from weather apps to social platforms. This guide demystifies REST, HTTP verbs, and authentication.",
    category: "TECH",
    tags: ["WEB DEV"],
    likes: 412,
    readTime: "15 min"
  };

  const sideList = [
    { id: "01", title: "CockroachDB vs PostgreSQL", cat: "Database" },
    { id: "02", title: "My Unsplash API Project", cat: "Project" },
    { id: "03", title: "OAuth 2.0 Explained Simply", cat: "Security" },
    { id: "04", title: "Nginx vs Apache: Real Tests", cat: "DevOps" }
  ];
</script>

<div class="space-y-10 animate-in fade-in duration-500">
  
  <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
    <div class="mb-8">
      <span class="text-[10px] font-black text-yellow-400 tracking-[0.2em] uppercase">Editor's Picks</span>
      <h1 class="text-4xl font-bold text-white mt-2">Featured Articles</h1>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <div class="lg:col-span-2 bg-black/20 rounded-[2rem] border border-white/5 p-8 flex flex-col justify-end min-h-[450px] relative overflow-hidden group">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-20 group-hover:scale-110 transition-transform duration-700">
          <span class="text-[120px]">🌐</span>
        </div>

        <div class="relative z-10">
          <div class="bg-yellow-400 text-black text-[10px] font-black px-3 py-1 rounded-md w-fit mb-6">✦ TOP OF THE WEEK</div>
          <div class="flex gap-2 mb-4">
             {#each featured.tags as tag}
               <span class="text-[10px] font-bold text-yellow-400/80 border border-yellow-400/20 px-2 py-0.5 rounded-md">{tag}</span>
             {/each}
          </div>
          <h2 class="text-3xl font-bold text-white mb-4 leading-tight">{featured.title}</h2>
          <p class="text-gray-400 max-w-xl mb-8">{featured.description}</p>
          
          <div class="flex items-center justify-between border-t border-white/10 pt-6">
            <button class="bg-yellow-400 text-black font-black px-6 py-3 rounded-xl hover:bg-yellow-300 transition-colors">READ FULL ARTICLE</button>
            <div class="text-gray-500 text-sm font-medium flex gap-4">
              <span>🕒 {featured.readTime}</span>
              <span>🔥 {featured.likes} likes</span>
            </div>
          </div>
        </div>
      </div>

      <div class="space-y-4">
        {#each sideList as item}
          <div class="bg-black/20 p-5 rounded-2xl border border-white/5 hover:border-white/20 transition-all cursor-pointer group">
            <div class="flex gap-4">
              <span class="text-2xl font-black text-white/10 group-hover:text-white/30 transition-colors">{item.id}</span>
              <div>
                <h3 class="text-white font-bold text-sm mb-1 leading-snug">{item.title}</h3>
                <span class="text-[10px] text-gray-500 font-bold uppercase tracking-widest">📁 {item.cat}</span>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <div class="flex items-center gap-4 px-4 overflow-x-auto pb-2 no-scrollbar">
    <button class="bg-white text-black px-6 py-2 rounded-full text-sm font-bold">All Posts</button>
    <button class="bg-white/5 hover:bg-white/10 px-6 py-2 rounded-full text-sm font-medium border border-white/5 transition-colors">Technology</button>
    <button class="bg-white/5 hover:bg-white/10 px-6 py-2 rounded-full text-sm font-medium border border-white/5 transition-colors">Productivity</button>
    <button class="bg-white/5 hover:bg-white/10 px-6 py-2 rounded-full text-sm font-medium border border-white/5 transition-colors">Health</button>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pb-20">
    </div>
</div>
