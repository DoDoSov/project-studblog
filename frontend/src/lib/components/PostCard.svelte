<script>
  import { imageFor, formatDate, readTime } from '../utils.js';

  /**
   * Svelte 4 Props
   */
  export let post = {};
  export let onRead = () => {};
  export let onSave = null;
  export let onLike = null;
  export let saved = false;
  export let liked = false;
</script>

<article class="glass-card group h-full flex flex-col overflow-hidden">
  <!-- Image Container -->
  <div class="relative h-48 overflow-hidden">
    <img 
      src={imageFor(post)} 
      alt={post.title} 
      class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
    />
    <div class="absolute inset-0 bg-gradient-to-t from-[#1A1F2E] to-transparent opacity-60"></div>
    <span class="absolute top-4 left-4 bg-blue-600 text-white text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-widest">
      {post.category}
    </span>
  </div>

  <div class="p-6 flex flex-col flex-grow">
    <!-- Meta Info -->
    <div class="text-[10px] font-black text-white/30 uppercase tracking-[0.2em] mb-3">
      {formatDate(post.created_at)} • {readTime(post.content)}
    </div>

    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-blue-400 transition-colors line-clamp-2">
      {post.title}
    </h3>

    <p class="text-sm text-white/50 leading-relaxed mb-6 line-clamp-3">
      {post.description || 'Open this student article to read the full post and explore the research.'}
    </p>

    <!-- Card Actions -->
    <div class="mt-auto pt-6 border-t border-white/5 flex items-center justify-between">
      <button 
        class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-xl text-xs font-bold transition-all active:scale-95"
        on:click={() => onRead(post)}
      >
        Read
      </button>

      <div class="flex gap-2">
        {#if onSave}
          <button 
            class="size-9 flex items-center justify-center rounded-xl border border-white/10 transition-all {saved ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-400' : 'bg-white/5 text-white/40 hover:text-white'}" 
            on:click={() => onSave(post)} 
            title="Read later"
          >
            🔖
          </button>
        {/if}
        
        {#if onLike}
          <button 
            class="size-9 flex items-center justify-center rounded-xl border border-white/10 transition-all {liked ? 'bg-red-500/20 border-red-500/50 text-red-400' : 'bg-white/5 text-white/40 hover:text-white'}" 
            on:click={() => onLike(post)} 
            title="Like"
          >
            ♥
          </button>
        {/if}
      </div>
    </div>
  </div>
</article>

<style>
  /* Tailwind 4.0 Glass Panel utility */
  .glass-card {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 2.5rem;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .glass-card:hover {
    border-color: rgba(59, 130, 246, 0.3);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  }
</style>