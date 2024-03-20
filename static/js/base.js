console.log("app started");

document.addEventListener("alpine:init", () => {
    console.log("Alpine Js Initialized");
  Alpine.data("base", () => ({
    text:"Text here",
    open: false,
    toggle() {
      this.open = !this.open;
    },
  }));
});
