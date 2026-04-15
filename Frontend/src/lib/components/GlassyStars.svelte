<script>
  // Grid settings
  const rows = 14;
  const cols = 8;
  const spawnChance = 0.3; // 30% chance a star exists in a grid cell

  // Generate the grid data once
  const grid = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (Math.random() < spawnChance) {
        grid.push({
          top: (r * (100 / rows)) + (Math.random() * 2), // Position + slight jitter
          left: (c * (100 / cols)) + (Math.random() * 2),
          delay: Math.random() * 5, // Random start for the shine
          duration: 3 + Math.random() * 4 // Random speed of the shine
        });
      }
    }
  }
</script>

<div class="fixed inset-0 w-full h-full -z-10 bg-[#0B0E14] overflow-hidden pointer-events-none">
  {#each grid as star}
    <div 
      class="absolute star-crystal"
      style="
        top: {star.top}%; 
        left: {star.left}%; 
        --delay: {star.delay}s; 
        --duration: {star.duration}s;
      "
    >
      <svg viewBox="0 0 100 100" class="size-12 text-blue-400/30">
        <path d="M50,15 C55,40 60,45 85,50 C60,55 55,60 50,85 C45,60 40,55 15,50 C40,45 45,40 50,15 Z" fill="currentColor" />
      </svg>
    </div>
  {/each}
</div>

<style>
  .star-crystal {
    animation: crystal-shine var(--duration) ease-in-out infinite;
    animation-delay: var(--delay);
    filter: blur(0.5px);
  }

  @keyframes crystal-shine {
    0%, 100% {
      opacity: 0.1;
      transform: scale(0.8) rotate(0deg);
      filter: brightness(1) blur(1px);
    }
    50% {
      opacity: 0.6;
      transform: scale(1.1) rotate(5deg);
      filter: brightness(2) blur(0px); /* The "Crystal" flash */
    }
  }
</style>