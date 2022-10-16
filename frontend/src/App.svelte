<script lang="ts">
  import Canvas from "./lib/Canvas.svelte";
  import Katex from "./lib/Katex.svelte";
  import Spinner from "./lib/Spinner.svelte";

  let latex: string | undefined;
  let loading = false;

  function predict() {
    loading = true;

    let canvas = document.getElementById("canvas") as HTMLCanvasElement;

    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append("image", blob);

      const resp = await fetch("http://localhost:8000/image", {
        method: "POST",
        body: formData,
      });
      latex = await resp.text();
      loading = false;
    });
  }
</script>

<main
  class="h-full max-w-4xl mx-auto p-8 flex flex-col items-center gap-4 justify-center"
>
  <h1 class="font-semibold text-5xl">TeXify</h1>
  <p class="text-gray-500 text-2xl mb-4">
    Easily convert handwritten math into <Katex math="\LaTeX" />.
  </p>

  <div class="h-96 self-stretch bg-white shadow-lg rounded-lg">
    <Canvas />
  </div>

  <div class="self-stretch flex gap-4">
    <div
      class="flex-1 bg-white rounded-lg shadow-lg p-4 font-mono self-stretch text-center"
    >
      {#if latex}
        {latex}
      {:else}
        <span class="text-gray-400">LaTeX will appear here</span>
      {/if}
    </div>

    <button
      class="bg-blue-500 p-4 h-full aspect-square rounded-lg shadow-lg text-white transition-all hover:bg-blue-600 hover:shadow-xl disabled:bg-blue-700 disabled:cursor-not-allowed"
      on:click={predict}
      disabled={loading}
    >
      {#if loading}
        <Spinner />
      {:else}
        Go
      {/if}
    </button>
  </div>

  <div
    class="self-stretch bg-white shadow-lg rounded-lg text-center h-48 flex items-center justify-center"
  >
    {#if latex}
      <span class="text-5xl"><Katex math={latex ?? ""} displayMode /></span>
    {:else}
      <span class="text-gray-400">Rendered math will appear here</span>
    {/if}
  </div>
</main>

<style>
  :global(.katex *) {
    border-color: black;
  }
</style>
