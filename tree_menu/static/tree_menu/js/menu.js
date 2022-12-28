const toggler = document.getElementsByClassName("caret");
for (let i = 0; i < toggler.length; i++) {
	toggler[i].addEventListener("click", () => {
		console.log(this);
		toggler[i].parentElement
			.querySelector(".nested")
			.classList.toggle("active");
	});
}
