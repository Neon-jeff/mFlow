// update input on change script

// let inputs = Array.from(document.querySelectorAll("input"));

// inputs.forEach((input) => {
//   input.addEventListener("input", (e) => {
//     input.value = e.target.value;
//   });
// });

// forms

document.addEventListener("alpine:init", () => {
  Alpine.data("base", () => ({
    showBaseLoader: false,
    showErrorLoader: false,
    errorText:"Something went wrong, reload and try again",
    open: false,
    toggle() {
      this.open = !this.open;
    },
    async signUp(e) {
      e.preventDefault();
      this.showBaseLoader = true;
      let regFormData = new FormData(document.querySelector(".regForm"));
      await fetch("", {
        method: "post",
        body: regFormData,
      })
        .then(async(res) => {
          if(res.status==400){
            this.showBaseLoader=false
            this.errorText="User with email already exists"
            this.showErrorLoader=true
          }
        })
        .catch((e) => console.error(e));
    },
  }));
});
