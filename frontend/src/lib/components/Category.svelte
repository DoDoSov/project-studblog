<script>
  import { CATEGORIES } from '../utils.js';

  /**
   * Svelte 4 Prop Migration
   */
  export let selected = 'All';
  export let onSelect = () => {};
</script>

<div class="category-row flex gap-3 overflow-x-auto pb-4 custom-scrollbar" aria-label="Post categories">
  {#each CATEGORIES as category}
    <button
      class="category-chip {selected === category ? 'active' : ''}"
      on:click={() => onSelect(category)}
    >
      {category}
    </button>
  {/each}
</div>

<style>
  @reference "../../app.css"; 
  /* Glassmorphism Styling matching your Gemini theme */
  .category-chip {
    @apply px-6 py-2 rounded-full text-xs font-black uppercase tracking-widest whitespace-nowrap
           transition-all duration-300 border border-white/5 bg-white/5 text-white/40
           hover:bg-white/10 hover:text-white hover:border-white/10;
  }

  .category-chip.active {
    @apply bg-blue-600 border-blue-500 text-white shadow-lg shadow-blue-500/20;
  }

  /* Hide scrollbar but keep functionality */
  .custom-scrollbar::-webkit-scrollbar {
    height: 4px;
    display: none;
  }
  
  .category-row:hover::-webkit-scrollbar {
    display: block;
  }

  .custom-scrollbar::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
  }
</style>