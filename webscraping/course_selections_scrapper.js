// yoinked from https://stackoverflow.com/a/39914235
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
	var catagories = document.getElementsByClassName("row align-justify align-middle app-c-accordion__head app-c-accordion__head--collapsed collapse")
	for (i = 0; i < catagories.length; i++) {
		catagories[i].click();
		await sleep(800);
	}
	var catagories = document.getElementsByClassName("courseItem")
	var details = []
	for (i = 0; i < catagories.length; i++) {
		catagories[i].click();
		await sleep(500)
		details.push(document.getElementsByClassName("courseDetails__content")[0].innerText)
		await sleep(500)
		document.getElementById("teacherDialogClose").click()
		await sleep(500)
	}

  	var hiddenElement = document.createElement('a');
  	hiddenElement.href = 'data:attachment/text,' + encodeURI(JSON.stringify(details));
  	hiddenElement.target = '_blank';
  	hiddenElement.download = 'scrapped.txt';
  	hiddenElement.click();
}

run();
