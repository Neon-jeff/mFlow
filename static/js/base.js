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
    errorText: "Something went wrong, reload and try again",
    open: false,
    toggle() {
      this.open = !this.open;
    },
    async verifyOtp(e) {
      e.preventDefault();
      this.showBaseLoader = true;
      let otpForm = new FormData(document.querySelector(".otpForm"));
      await fetch("", {
        method: "post",
        body: otpForm,
      })
        .then(async (res) => {
          if (res.status == 400) {
            this.showBaseLoader = false;
            this.errorText = "Invalid OTP provided";
            this.showErrorLoader = true;
          } else {
            location.assign(`${location.origin}/dashboard`);
          }
        })
        .catch((e) => console.error(e));
    },
    async signUp(e) {
      e.preventDefault();
      this.showBaseLoader = true;
      let regFormData = new FormData(document.querySelector(".regForm"));
      await fetch("", {
        method: "post",
        body: regFormData,
      })
        .then(async (res) => {
          if (res.status == 400) {
            this.showBaseLoader = false;
            this.errorText = "User with email already exists";
            this.showErrorLoader = true;
          } else {
            location.assign(`${location.origin}/auth/verify-email/`);
          }
        })
        .catch((e) => console.error(e));
    },
  }));
});
