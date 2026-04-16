<script>
  let { postData = {
    title: "Getting Started with JavaScript in 2026",
    description: "A beginner-friendly guide to understanding the basics of JavaScript and building your first interactive web page.",
    tags: ["JavaScript", "WebDevelopment", "#Beginner", "#Coding"],
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere.",
    author: "Author's Name",
    authorBio: "Position/Short bio. Lorem ipsum dolor sit amet consectetur adipiscing elit.",
    outline: ["Introduction", "Variables", "Functions", "Loops", "DOM Manipulation", "Next Steps"]
  }} = $props();
</script>

<div class="h-32"></div>

<div class="max-w-7xl mx-auto px-4 md:px-6 pb-20">
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 font-sans text-white">
    
    <div class="lg:col-span-2 flex flex-col gap-6">
      
      <div class="bg-white/10 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem] shadow-xl">
        <h1 class="text-3xl md:text-4xl font-bold leading-tight">
          {postData.title}
        </h1>
      </div>

      <div class="bg-[#2D364F]/50 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem]">
        <p class="text-lg text-gray-200 leading-relaxed mb-4">
          <span class="font-bold text-white">Description:</span> {postData.description}
        </p>
        <div class="flex flex-wrap gap-3">
          {#each postData.tags as tag}
            <span class="text-sm text-gray-400 italic">#{tag.replace('#', '')}</span>
          {/each}
        </div>
      </div>

      <div class="bg-white/5 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem] min-h-[400px]">
        <div class="text-gray-300 leading-[1.8] space-y-6 text-lg">
          <p>{postData.content}</p>
          <p>{postData.content}</p>
          <p>{postData.content}</p>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-6">
      
      <div class="bg-[#2D364F]/80 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem] shadow-xl">
        <h3 class="text-xl font-bold mb-6">Post Content:</h3>
        <ol class="space-y-3">
          {#each postData.outline as item, i}
            <li class="flex gap-3 text-gray-300 hover:text-white transition-colors cursor-pointer group">
              <span class="font-bold text-white/50">{i + 1}.</span>
              <span>{item}</span>
            </li>
          {/each}
        </ol>
      </div>

      <div class="bg-[#3D4766]/50 backdrop-blur-md border border-white/10 p-8 rounded-[2.5rem] flex flex-col items-center text-center">
        <div class="size-24 bg-gray-500/50 rounded-full mb-6 flex items-center justify-center border-4 border-white/10 shadow-inner overflow-hidden">
            <svg class="size-14 text-white/40" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
        </div>

        <h3 class="text-2xl font-bold mb-1">{postData.author}</h3>
        <p class="text-xs font-black text-purple-400 uppercase tracking-widest mb-4">{postData.authorBio.split('.')[0]}</p>
        
        <p class="text-sm text-gray-400 leading-relaxed">
          {postData.authorBio}
        </p>
      </div>

    </div>
  </div>
</div>

<style>
  /* Optional: Smooth fade-in for the bento boxes */
  div {
    animation: fadeIn 0.6s ease-out;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>