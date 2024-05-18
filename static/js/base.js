

document.addEventListener("alpine:init", () => {
  Alpine.data("base", () => ({
    text: "Text here",
    open: false,
    toggle() {
      this.open = !this.open;
    },
  }));
});
