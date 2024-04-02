let btnList = Array.from(document.querySelector(".scrollList").children);



const emblaNode = document.querySelector(".embla");
const options = { loop: false };
const plugins = [EmblaCarouselAutoplay()];
const emblaApi = EmblaCarousel(emblaNode, options);

emblaApi.on('scroll',()=>{
    btnList.forEach(btn=>{
        if(btn.id==emblaApi.selectedScrollSnap()){
            btn.classList.remove('bg-accent')
            btn.classList.add('bg-main')
        }
        else{
              btn.classList.remove("bg-main");
              btn.classList.add("bg-accent");
        }
    })
})

btnList.forEach(btn=>{
    btn.addEventListener('click',()=>{
        emblaApi.scrollTo(parseInt(btn.id), false);
    })
})
