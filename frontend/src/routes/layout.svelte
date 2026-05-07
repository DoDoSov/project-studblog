<script>
  import "../app.css";
  import GlassyStars from "../lib/components/GlassyStars.svelte";

  let { children } = $props();
</script>

<!-- The background stays fixed across all navigation -->
<GlassyStars />

<!-- The page content renders on top -->
<main class="relative z-10">
  {@render children()}
</main>