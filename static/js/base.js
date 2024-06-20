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
    showMobileNav:false,
    showBaseLoader: false,
    showErrorLoader: false,
    errorText: "Something went wrong, reload and try again",
    open: false,
    account_type: null,

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
            location.assign(`${location.origin}/auth/choose/`);
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
    async login(e) {
      e.preventDefault();
      this.showBaseLoader = true;
      let loginFormData = new FormData(document.querySelector(".login"));
      await fetch("", { method: "post", body: loginFormData })
        .then(async (res) => {
          if (res.status == 400) {
            this.showBaseLoader = false;
            this.errorText = "Invalid Login Details";
            this.showErrorLoader = true;
          } else {
            location.assign(`${location.origin}/dashboard/`);
          }
        })
        .catch((e) => console.error(e));
    },
    chooseAccountType(el) {
      if (el.classList.contains("vendor")) {
        this.account_type = "vendor";
        el.classList.add("border-2", "border-main");
        el.children[0].classList.add("bg-main");
        el.previousElementSibling.classList.remove("border-2");
        el.previousElementSibling.children[0].classList.remove("bg-main");
      } else if (el.classList.contains("affiliate")) {
        this.account_type = "affiliate";
        el.classList.add("border-2", "border-main");
        el.children[0].classList.add("bg-main");
        el.nextElementSibling.classList.remove("border-2");
        el.nextElementSibling.children[0].classList.remove("bg-main");
      }
    },
    async completeOnboarding() {
      if (this.account_type == null) {
        this.errorText = "Select an account type";
        this.showErrorLoader = true;
        return;
      }
      const formdata = new FormData();
      formdata.set("account_type", this.account_type);
      this.showBaseLoader = true;
      await fetch("", {
        method: "post",
        body: formdata,
      }).then(async (res) => {
        if (res.ok) {
          location.assign(`${location.origin}/dashboard/`);
        } else {
          this.showBaseLoader = false;
          this.errorText = "Connection problems, please try again";
        }
      });
    },
  }));
});
