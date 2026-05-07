<script>
  import { onMount } from 'svelte';

  // State variables to hold the API data
  let aboutData = {
    mission: "Loading...",
    active_writers: "...",
    steps: []
  };

  async function fetchAboutContent() {
    try {
      // Connect to the Static HTML API endpoint
      const response = await fetch('/api/about-static');
      if (response.ok) {
        aboutData = await response.json();
      }
    } catch (err) {
      console.error("Failed to load static about content:", err);
    }
  }

  onMount(() => {
    fetchAboutContent();
  });
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 mb-20 space-y-12">
  <!-- Hero Section -->
  <div class="glass-panel p-10 md:p-20 rounded-[3rem] relative overflow-hidden">
    <div class="relative z-10 max-w-3xl">
      <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase mb-4">How it works</p>
      <h1 class="text-5xl md:text-7xl font-black text-white leading-tight mb-8">
        Built for <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">Students</span>
      </h1>
      <p class="text-white/50 text-xl leading-relaxed">
        StudBlogs is modeled after the best parts of Dev.to and Hackernoon — open, community-driven, and free. We provide a space for academic insights and student life.
      </p>
    </div>
    <!-- Background Icon for aesthetic -->
    <div class="absolute -right-16 -bottom-16 opacity-5 text-[300px] pointer-events-none rotate-12 select-none">🎓</div>
  </div>

  <!-- Step Cards Grid (Rendered from Static API) -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    {#each aboutData.steps as step}
      <div class="glass-panel p-8 rounded-[2.5rem] hover:border-blue-500/40 transition-all duration-500 group">
        <div class="text-5xl mb-8 group-hover:scale-110 group-hover:-rotate-6 transition-transform duration-300 inline-block">
          {step.icon}
        </div>
        <p class="text-[10px] font-black text-blue-400 tracking-widest uppercase mb-2">{step.id}</p>
        <h3 class="text-xl font-bold text-white mb-4">{step.title}</h3>
        <p class="text-white/40 text-sm leading-relaxed">{step.desc}</p>
      </div>
    {/each}
  </div>

  <!-- Stats and Mission (Rendered from Static API) -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
    <div class="lg:col-span-2 bg-purple-600/10 border border-purple-500/20 p-12 rounded-[3rem] flex flex-col justify-center">
        <h2 class="text-3xl font-bold text-white mb-4">Our Core Mission</h2>
        <p class="text-purple-200/60 text-xl leading-relaxed">{aboutData.mission}</p>
    </div>
    <div class="glass-panel p-12 rounded-[3rem] flex items-center justify-center text-center">
        <div>
          <p class="text-5xl font-black text-white">{aboutData.active_writers}</p>
          <p class="text-xs text-white/30 uppercase tracking-[0.2em] font-bold mt-4">Active Writers</p>
        </div>
    </div>
  </div>
</section>

<style>
  /* Tailwind Glass Effect */
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>