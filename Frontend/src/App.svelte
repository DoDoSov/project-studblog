<script>
  import GlassyStars from './lib/components/GlassyStars.svelte';
  import Branding from './lib/components/Branding.svelte';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';
  
  // Views
  import HomeView from './routes/Main.svelte';
  import ReadPage from './routes/ReadPage.svelte'; // Assuming you created this file

  // Svelte 5 state for navigation
  let currentTab = $state("Home");
</script>

<Branding />
<GlassyStars />

<Navbar bind:activeTab={currentTab} />

<main>
  {#if currentTab === "Home"}
    <HomeView />
  {:else if currentTab === "Read"}
    <ReadPage />
  {:else}
    <div class="h-screen flex items-center justify-center text-white/20 uppercase tracking-widest">
      {currentTab} Section Coming Soon
    </div>
  {/if}
</main>

<Footer />

<style lang="postcss">
  @reference "tailwindcss";
</style>