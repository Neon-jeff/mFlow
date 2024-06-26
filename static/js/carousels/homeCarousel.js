let btnList = Array.from(document.querySelector(".scrollList").children);

const emblaNode = document.querySelector(".embla");
const options = { loop: false };
const plugins = [EmblaCarouselAutoplay()];
const emblaApi = EmblaCarousel(emblaNode, options);

emblaApi.on("scroll", () => {
  btnList.forEach((btn) => {
    if (btn.id == emblaApi.selectedScrollSnap()) {
      btn.classList.remove("bg-neutral-400");
      btn.classList.add("bg-dark");
    } else {
      btn.classList.remove("bg-dark");
      btn.classList.add("bg-neutral-400");
    }
  });
});

btnList.forEach((btn) => {
  btn.addEventListener("click", () => {
    emblaApi.scrollTo(parseInt(btn.id), false);
  });
});
