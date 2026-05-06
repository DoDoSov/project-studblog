<script>

</script>

<main class="min-h-screen flex flex-col items-center justify-center bg-[#050505] text-white px-6">
  <!-- Decorative background element -->
  <div class="absolute inset-0 overflow-hidden pointer-events-none">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-blue-600/10 blur-[120px] rounded-full"></div>
  </div>

  <div class="relative z-10 text-center">
    <h1 class="text-[12rem] font-black leading-none tracking-tighter opacity-10">
      404
    </h1>
    
    <div class="mt-[-4rem]">
      <h2 class="text-4xl font-bold mb-4">Lost in Space?</h2>
      <p class="text-gray-400 max-w-md mx-auto mb-8">
        The page you are looking for doesn't exist or has been moved to another coordinate.
      </p>

      <a 
        href="/" 
        class="inline-block px-8 py-4 bg-white text-black font-bold rounded-2xl transition-transform hover:scale-105 active:scale-95"
      >
        Return to Home
      </a>
    </div>
  </div>
</main>

<style>
  /* Optional: Custom font or animations for the 404 number */
  h1 {
    user-select: none;
    background: linear-gradient(to bottom, white, transparent);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
</style>