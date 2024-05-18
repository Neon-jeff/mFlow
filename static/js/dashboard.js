document.addEventListener("alpine:init", () => {
  Alpine.data("dashboard", () => ({
    drawerOpen: false,
    profileOptionsOpen:false
  }));
});
