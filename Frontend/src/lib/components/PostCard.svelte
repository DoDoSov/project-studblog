<script>
  // These are "props" - they let us pass different data to each card
  let { image, title, description, tags = [] } = $props();
</script>

<div class="bg-[#2D364F]/50 rounded-3xl overflow-hidden border border-white/5 flex flex-col h-full hover:scale-[1.02] transition-transform duration-300">
  <div class="relative h-48 w-full">
    <img src={image} alt={title} class="w-full h-full object-cover" />
    <div class="absolute inset-0 bg-gradient-to-t from-[#2D364F] to-transparent opacity-60"></div>
  </div>

  <div class="p-5 flex flex-col flex-grow">
    <h3 class="text-xl font-bold leading-tight mb-2 text-white">
      {title}
    </h3>
    <p class="text-gray-400 text-sm line-clamp-2 mb-4">
      {description}
    </p>

    <div class="flex flex-wrap gap-2 mb-6">
      {#each tags as tag}
        <span class="text-[10px] text-gray-500 font-mono">#{tag}</span>
      {/each}
    </div>

    <div class="mt-auto flex items-center justify-between pt-4 border-t border-white/10">
      <div class="flex gap-4 opacity-70">
        <button class="hover:text-blue-400">🔗</button>
        <button class="hover:text-yellow-400">🔖</button>
        <button class="hover:text-red-400">❤️</button>
      </div>
      <button class="bg-white text-black text-xs font-bold px-4 py-2 rounded-full hover:bg-gray-200 transition">
        Read
      </button>
    </div>
  </div>
</div>