// yoinked from https://stackoverflow.com/a/39914235
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
	var pages = Number(document.getElementsByClassName("pageTrack")[0].innerText.split(" ")[2])
	var details = []
	for (ii = 0; ii < pages; ii++) {
		var choice = document.getElementsByClassName("openEntityInPanel Program")
		var currentProgram = []
		for (i = 0; i < choice.length; i++) {
			choice[i].click();
			await sleep(6000)
			currentProgram.push(document.getElementsByClassName("headerTitle")[0].innerText.split("\n"))
			// map() = https://stackoverflow.com/a/33873355
			// filter() = https://stackoverflow.com/a/281335
			// trim() = https://stackoverflow.com/a/498995
			currentProgram.push(document.getElementsByClassName("large-8 medium-12 small-12 columns end")[0].firstElementChild.innerText.split("\n").filter(Boolean).map((string) => string.trimRight()))
			currentProgram.push(document.getElementsByClassName("large-8 medium-12 small-12 columns end")[0].firstElementChild.nextElementSibling.innerText.split("\n").filter(Boolean).map((string) => string.trimRight()))
			document.getElementsByClassName("ui-tabs-nav ui-helper-reset ui-helper-clearfix ui-widget-header ui-corner-all")[2].firstElementChild.nextElementSibling.firstElementChild.click()
			await sleep(1000)
			currentProgram.push([document.getElementsByClassName("small-12 columns empty-requirements")[0].firstElementChild.nextElementSibling.nextElementSibling.innerText.split("\n").filter(Boolean).map((string) => string.trimRight())])
			document.getElementsByClassName("backBtn")[0].click()
			await sleep(500)
			details.push(currentProgram)
			console.log("page", ii+1, "progList", i+1)
		}
		document.getElementsByClassName("nextPage changePage button tertiary float-right")[0].click()
		await sleep(3000)
	}

  	var hiddenElement = document.createElement('a');
  	hiddenElement.href = 'data:attachment/text,' + encodeURI(JSON.stringify(details));
  	hiddenElement.target = '_blank';
  	hiddenElement.download = 'scrapped.txt';
  	hiddenElement.click();
}

run();
