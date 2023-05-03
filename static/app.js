class BoggleGame {
	constructor(boardId, secs = 60) {
		this.secs = secs;
		this.board = $("#" + boardId);
		this.score = 0;

		$(".check-word", this.board).on("submit", this.handleSubmit.bind(this));
	}

	runme() {
		// This is just so I can see the jquery object
		console.log(this.board);
		console.log(this.board.get(0));
	}

	showMessage(msg, cls) {
		$(".msg", this.board).text(msg).removeClass().addClass(`msg ${cls}`);
	}

	showScore(score) {
		$(".score", this.board).text(score);
	}

	async handleSubmit(evt) {
		evt.preventDefault();
		const $word = $(".word", this.board);
		let word = $word.val().toLowerCase();
		const resp = await axios.get("/check-word", { params: { word: word } });

		if (resp.data.result === "not-word") {
			this.showMessage(`${word} is not a valid English word`, "err");
		} else if (resp.data.result === "not-on-board") {
			this.showMessage(`${word} is not a valid word on this board`, "err");
		} else {
			this.showMessage(`Added: ${word}`, "ok");
			this.score += word.length;
			this.showScore(this.score);
			// console.log(this.score);
		}

		$word.val("").focus();
	}
}

$(".restart").on("click", handleReset());

function handleReset() {
	game = new BoggleGame("boggle", 60);
}
