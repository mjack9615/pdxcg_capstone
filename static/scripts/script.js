const api_kw = document.querySelector("#api_kw_sub")
const api_ss = document.querySelector("#api_ss_sub")
const api_tr = document.querySelector("#api_tr_sub")
const kw_input = document.querySelector("#kw_input")
const ss_input = document.querySelector("#ss_input")
const tr_input = document.querySelector("#tr_input")


function getKw() {
	api_kw.innerHTML = ""
	let search = kw_input.value
	fetch(`https://api.rawg.io/api/games?key=4fae09a36f754b5bb3540f93edd09f3a&search=${search}&page_size=500`)
	.then((response) => response.json())
	.then((data) => {
		for (let i = 0; i < data.results.length; i++) {
			api_kw.innerHTML += "<br>" + data.results[i].name + ", " + data.results[i].platforms[0].platform.name + ", " + data.results[i].metacritic
		}	
	})
}	

function getSs() {
	api_ss.innerHTML = ""
	let game_pk = ss_input.value
	fetch(`https://api.rawg.io/api/games/${game_pk}/screenshots?key=4fae09a36f754b5bb3540f93edd09f3a`)
	.then((response) => response.json())
	.then((data) => {
		for (let i = 0; i < data.results.length; i++) {
			api_ss.innerHTML += "<br>" + "<a href='"  + data.results[i].image + "'>" + data.results[i].image + "</a>"
		}	
	})
}	

function getTr() {
	api_tr.innerHTML = ""
	let id = tr_input.value
	fetch(`https://api.rawg.io/api/games/${id}/movies?key=4fae09a36f754b5bb3540f93edd09f3a`)
	.then((response) => response.json())
	.then((data) => {
		for (let i = 0; i < data.results.length; i++) {
			api_tr.innerHTML += "<br>" + "<a href='" + data['results'][i]['data']['480'] + "'>" + data['results'][i]['data']['480'] + "</a>"
		}	
	})
}	