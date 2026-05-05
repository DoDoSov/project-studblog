<script>
  import { formatDate, readTime } from '../utils.js';

  // Svelte 4 Props
  export let post = {};
  export let onRead = () => {};
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<article 
  class="glass-card-compact" 
  on:click={() => onRead(post)} 
  role="button" 
  tabindex="0"
>
  <!-- Category Avatar -->
  <div class="size-10 shrink-0 bg-blue-600/20 border border-blue-500/30 rounded-xl flex items-center justify-center text-blue-400 font-black text-xs">
    {(post.category || 'B').slice(0, 2).toUpperCase()}
  </div>

  <div class="flex-grow min-w-0">
    <div class="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest mb-1">
      <span class="text-blue-400">{post.category}</span>
      <span class="size-1 bg-white/10 rounded-full"></span>
      <span class="text-white/30">{formatDate(post.created_at)}</span>
    </div>
    
    <h3 class="text-white font-bold text-sm leading-tight truncate group-hover:text-blue-400 transition-colors">
      {post.title}
    </h3>
    
    <p class="text-[10px] text-white/30 mt-1 truncate">
      {post.author || 'Student writer'} • {readTime(post.content)}
    </p>
  </div>
</article>

<style>
  @reference "../../app.css"; 
  /* Tailwind 4.0 Compact Glass Utility */
  .glass-card-compact {
    @apply flex items-center gap-4 p-4 rounded-[1.5rem] bg-white/5 border border-white/5 
           hover:bg-white/10 hover:border-white/10 transition-all cursor-pointer ;
    backdrop-filter: blur(8px);
  }
</style>