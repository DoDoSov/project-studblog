<script>
  import LeftArrow from '../../assets/Category/left-arrow.svg';
  import RightArrow from '../../assets/Category/right-arrow.svg';

  // Props for Svelte 5
  let { onSelect = (cat) => {} } = $props();

  let categories = ["Technology", "Finance", "Business", "Health", "Travel", "Science", "Education", "Lifestyle", "Engineering", "Sports", "AI"];
  let active = $state("Technology");
  let scrollContainer = $state();

  function scroll(direction) {
    const amount = 200;
    scrollContainer.scrollBy({
      left: direction === 'left' ? -amount : amount,
      behavior: 'smooth'
    });
  }

  function handleSelect(cat) {
    active = cat;
    onSelect(cat); // Send the category up to HomeView
  }
</script>

<div class="mx-2 md:mx-4 mb-6 sticky top-24 z-30">
  <div class="bg-[#1A1F2E]/80 backdrop-blur-xl p-1.5 rounded-2xl border border-white/5 flex items-center gap-1 shadow-2xl">
    
    <button 
      onclick={() => scroll('left')}
      class="hidden md:block p-2.5 hover:bg-white/5 rounded-xl transition-colors group shrink-0"
    >
      <img src={LeftArrow} class="size-4 opacity-50 group-hover:opacity-100 brightness-200" alt="Prev" />
    </button>

    <div class="flex-grow overflow-hidden relative">
      <div class="absolute left-0 top-0 bottom-0 w-8 bg-gradient-to-r from-[#1A1F2E] to-transparent z-10 pointer-events-none md:hidden"></div>
      
      <ul 
        bind:this={scrollContainer}
        class="flex items-center gap-1 overflow-x-auto no-scrollbar whitespace-nowrap py-1 px-4 md:px-0 scroll-smooth"
      >
        {#each categories as cat}
          <li>
            <button 
              onclick={() => handleSelect(cat)}
              class="px-5 py-2 rounded-xl text-xs md:text-sm font-bold transition-all duration-300
              {active === cat 
                ? 'bg-blue-600 text-white shadow-lg shadow-blue-900/20 scale-105' 
                : 'text-gray-400 hover:text-gray-200 hover:bg-white/5'}"
            >
              {cat}
            </button>
          </li>
        {/each}
      </ul>

      <div class="absolute right-0 top-0 bottom-0 w-8 bg-gradient-to-l from-[#1A1F2E] to-transparent z-10 pointer-events-none md:hidden"></div>
    </div>

    <button 
      onclick={() => scroll('right')}
      class="hidden md:block p-2.5 hover:bg-white/5 rounded-xl transition-colors group shrink-0"
    >
      <img src={RightArrow} class="size-4 opacity-50 group-hover:opacity-100 brightness-200" alt="Next" />
    </button>

  </div>
</div>

<style>
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>