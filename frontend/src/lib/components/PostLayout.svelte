<script>
  /**
   * Svelte 4 Props
   * We use 'export let' to define properties passed from parent components.
   */
  export let postData = {
    title: "Getting Started with JavaScript in 2026",
    description: "A beginner-friendly guide to understanding the basics of JavaScript and building your first interactive web page.",
    tags: ["JavaScript", "WebDevelopment", "Beginner", "Coding"],
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis.",
    author: "Author's Name",
    authorBio: "Position/Short bio. Lorem ipsum dolor sit amet consectetur adipiscing elit.",
    outline: ["Introduction", "Variables", "Functions", "Loops", "DOM Manipulation", "Next Steps"]
  };
</script>

<div class="h-32"></div>

<div class="max-w-7xl mx-auto px-4 md:px-6 pb-20">
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 font-sans text-white">
    
    <!-- Main Content Area -->
    <div class="lg:col-span-2 flex flex-col gap-6">
      
      <!-- Title Card -->
      <div class="glass-panel p-8 md:p-12 rounded-[3rem]">
        <h1 class="text-3xl md:text-5xl font-black leading-tight">
          {postData.title}
        </h1>
      </div>

      <!-- Description & Tags -->
      <div class="bg-[#2D364F]/50 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem]">
        <p class="text-lg text-white/70 leading-relaxed mb-6">
          <span class="font-bold text-white">Description:</span> {postData.description}
        </p>
        <div class="flex flex-wrap gap-3">
          {#each postData.tags as tag}
            <span class="text-xs font-bold text-blue-400 bg-blue-500/10 px-3 py-1 rounded-full uppercase tracking-tighter">
              #{tag.replace('#', '')}
            </span>
          {/each}
        </div>
      </div>

      <!-- Article Body -->
      <div class="glass-panel p-8 md:p-12 rounded-[3rem] min-h-[500px]">
        <div class="text-white/60 leading-[1.8] space-y-8 text-lg">
          <!-- Standard Svelte 4 each loops for content blocks[cite: 1] -->
          <p>{postData.content}</p>
          <p>{postData.content}</p>
          <p>{postData.content}</p>
        </div>
      </div>
    </div>

    <!-- Sidebar Area -->
    <div class="flex flex-col gap-6">
      
      <!-- Table of Contents -->
      <div class="bg-[#2D364F]/80 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem] shadow-xl">
        <h3 class="text-xl font-bold mb-6 text-blue-400 uppercase tracking-widest text-xs">Table of Contents</h3>
        <ol class="space-y-4">
          {#each postData.outline as item, i}
            <li class="flex gap-4 text-white/50 hover:text-white transition-all cursor-pointer group">
              <span class="font-black text-blue-500/50 group-hover:text-blue-400">0{i + 1}</span>
              <span class="font-medium">{item}</span>
            </li>
          {/each}
        </ol>
      </div>

      <!-- Author Card -->
      <div class="glass-panel p-10 rounded-[3rem] flex flex-col items-center text-center">
        <div class="size-24 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full mb-6 flex items-center justify-center border-4 border-white/10 shadow-xl">
            <svg class="size-12 text-white" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
        </div>

        <h3 class="text-2xl font-bold mb-1">{postData.author}</h3>
        <p class="text-[10px] font-black text-purple-400 uppercase tracking-[0.2em] mb-4">
          {postData.authorBio.split('.')[0]}
        </p>
        
        <p class="text-sm text-white/40 leading-relaxed">
          {postData.authorBio}
        </p>
      </div>

    </div>
  </div>
</div>

<style>
  /* Svelte 4 standard CSS animation[cite: 1] */
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    animation: fadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>