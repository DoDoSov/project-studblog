<script>
 

  // Sample data for posts created by the user
  let myPosts = $state([
    { id: 1, title: "My Journey into Svelte 5", status: "Published", date: "Oct 12, 2025", views: 1240 },
    { id: 2, title: "Understanding Tailwind v4 Engine", status: "Draft", date: "Oct 14, 2025", views: 0 },
    { id: 3, title: "Building a Bento Grid Portfolio", status: "Published", date: "Sep 28, 2025", views: 856 }
  ]);

  function handleCreate() {
    console.log("Navigating to Editor...");
  }

  function handleEdit(id) {
    console.log("Editing post:", id);
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl bg-[#283047] rounded-2xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  
  <div class="h-4"></div>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10">
    <div class="lg:col-span-2 bg-[#1A1F2E] p-10 rounded-[2.5rem] border border-white/5 shadow-2xl flex flex-col justify-center relative overflow-hidden">
      <div class="relative z-10">
        <p class="text-[10px] font-black text-blue-400 tracking-[0.2em] uppercase mb-4">Creator Studio</p>
        <h1 class="text-4xl font-bold text-white mb-4">Your Stories</h1>
        <p class="text-gray-400 max-w-md">Manage your drafts, view analytics, and share your knowledge with the student community.</p>
      </div>
      <span class="absolute -right-4 -bottom-10 text-[180px] opacity-5 pointer-events-none">Write</span>
    </div>

    <button 
      onclick={handleCreate}
      class="bg-blue-600 hover:bg-blue-500 transition-all rounded-[2.5rem] flex flex-col items-center justify-center p-10 group cursor-pointer shadow-xl shadow-purple-900/20"
    >
      <div class="size-16 bg-white/20 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
        <span class="text-3xl text-white">+</span>
      </div>
      <span class="text-xl font-bold text-white">Create New Post</span>
    </button>
  </div>

  <div class="bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 overflow-hidden shadow-2xl">
    <div class="p-8 border-b border-white/5 bg-white/5 flex justify-between items-center">
      <h2 class="font-bold text-white">Active Manuscripts</h2>
      <div class="flex gap-2">
        <span class="px-3 py-1 bg-black/20 rounded-full text-[10px] font-bold text-gray-400 uppercase tracking-widest border border-white/5">
          Total: {myPosts.length}
        </span>
      </div>
    </div>

    <div class="divide-y divide-white/5">
      {#each myPosts as post}
        <div class="p-6 hover:bg-white/[0.02] transition-colors flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="flex flex-col gap-1">
            <div class="flex items-center gap-3">
              <span class="text-sm font-bold text-white">{post.title}</span>
              <span class="text-[9px] font-black px-2 py-0.5 rounded {post.status === 'Published' ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'} uppercase tracking-tighter">
                {post.status}
              </span>
            </div>
            <p class="text-[10px] text-gray-500 font-medium">Last updated: {post.date} • {post.views} views</p>
          </div>

          <div class="flex items-center gap-2">
            <button 
              onclick={() => handleEdit(post.id)}
              class="p-3 bg-white/5 hover:bg-white/10 rounded-xl transition-all border border-white/5 text-gray-300 hover:text-white"
              title="Edit Post"
            >
              <div class="">Edit</div>
            </button>
            <button 
              class="p-3 bg-white/5 hover:bg-white/10 rounded-xl transition-all border border-white/5 text-gray-300 hover:text-white"
              title="View Analytics"
            >
              <div class="">View</div>
            </button>
            <button 
              class="p-3 bg-red-500/10 hover:bg-red-500/20 rounded-xl transition-all border border-red-500/10 text-red-400"
              title="Delete Post"
            >
              <div class="">Delete</div>
            </button>
          </div>
        </div>
      {/each}
    </div>
    
  </div>
  <div class="h-4"></div>
</section>