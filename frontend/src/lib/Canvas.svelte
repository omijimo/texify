<script lang="ts">
  let canvas: HTMLCanvasElement;
  let ctx: CanvasRenderingContext2D;
  let rect: DOMRect;
  let drawing = false;

  $: console.log(canvas);

  $: if (canvas) {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }

  $: if (canvas) {
    rect = canvas.getBoundingClientRect();
    ctx = canvas.getContext("2d");
    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.strokeStyle = "#c0392b";
  }

  function onMouseMove(e: MouseEvent) {
    if (!drawing) return;
    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.stroke();
  }

  function onMouseDown(e: MouseEvent) {
    drawing = true;
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.beginPath();
  }

  function onMouseUp(e: MouseEvent) {
    drawing = false;
  }
</script>

<canvas
  id="canvas"
  class="h-full w-full"
  bind:this={canvas}
  on:mousemove={onMouseMove}
  on:mousedown={onMouseDown}
  on:mouseup={onMouseUp}
/>
