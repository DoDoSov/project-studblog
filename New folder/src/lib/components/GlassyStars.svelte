<script>
  const rows = 12;
  const cols = 7;
  const spawnChance = 0.25;

  const grid = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (Math.random() < spawnChance) {
        grid.push({
          top: (r * (100 / rows)) + (Math.random() * 4),
          left: (c * (100 / cols)) + (Math.random() * 4),
          delay: Math.random() * -10,
          duration: 5 + Math.random() * 5,
          size: 20 + Math.random() * 30,
          rotation: Math.random() * 360
        });
      }
    }
  }
</script>

<div class="fixed inset-0 w-full h-full -z-10 bg-[#0B0E14] overflow-hidden pointer-events-none perspective-container">
  {#each grid as star}
    <div 
      class="absolute gemini-wrapper"
      style="
        top: {star.top}%; 
        left: {star.left}%; 
        --delay: {star.delay}s; 
        --duration: {star.duration}s;
        --size: {star.size}px;
        --init-rot: {star.rotation}deg;
      "
    >
      <!-- The Gemini Star Shape -->
      <svg 
        viewBox="0 0 100 100" 
        class="gemini-star"
        fill="none" 
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <radialGradient id="starGradient">
            <stop offset="0%" stop-color="#FFF" />
            <stop offset="40%" stop-color="#A78BFA" /> <!-- Purple from image -->
            <stop offset="100%" stop-color="#3B82F6" /> <!-- Blue from image -->
          </radialGradient>
          <filter id="glow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        <path 
          d="M50 0C50 27.6142 72.3858 50 100 50C72.3858 50 50 72.3858 50 100C50 72.3858 27.6142 50 0 50C27.6142 50 50 27.6142 50 0Z" 
          fill="url(#starGradient)"
          filter="url(#glow)"
        />
      </svg>
    </div>
  {/each}
</div>

<style>
  .perspective-container {
    perspective: 1200px;
  }

  .gemini-wrapper {
    width: var(--size);
    height: var(--size);
    /* Floating 3D movement */
    animation: float-3d var(--duration) ease-in-out infinite alternate;
    animation-delay: var(--delay);
    filter: drop-shadow(0 0 8px rgba(167, 139, 250, 0.4));
  }

  .gemini-star {
    width: 100%;
    height: 100%;
    /* Blinking effect */
    animation: gemini-blink var(--duration) ease-in-out infinite;
    animation-delay: var(--delay);
  }

  @keyframes float-3d {
    0% {
      transform: 
        translateY(0) 
        rotateX(0deg) 
        rotateY(0deg) 
        rotateZ(var(--init-rot));
    }
    100% {
      transform: 
        translateY(-40px) 
        rotateX(25deg) 
        rotateY(25deg) 
        rotateZ(calc(var(--init-rot) + 20deg));
    }
  }

  @keyframes gemini-blink {
    0%, 100% {
      opacity: 0.2;
      transform: scale(0.85);
      filter: brightness(0.8) blur(1px);
    }
    50% {
      opacity: 1;
      transform: scale(1.1);
      filter: brightness(1.4) blur(0px);
    }
  }
</style>