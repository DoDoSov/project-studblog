<script>
  import Navbar from '$lib/components/Navbar.svelte';
  import Toast from '$lib/components/Toast.svelte';
</script>

<Navbar />
<slot />
<Toast />

<style>
  :global(body) {
    background: #1a1d35;
    color: white;
  }
</style>