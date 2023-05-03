class BoggleGame {
	constructor(boardId, secs = 60) {
		this.secs = secs;
		this.showTimer();
		this.board = $("#" + boardId);
		this.score = 0;
		this.words = new Set();

		this.timer = setInterval(this.tick.bind(this), 1000);

		$(".check-word", this.board).on("submit", this.handleSubmit.bind(this));
	}

	showMessage(msg, cls) {
		$(".msg", this.board).text(msg).removeClass().addClass(`msg ${cls}`);
	}

	showTimer() {
		$(".timer", this.board).text(this.secs);
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
			if (this.words.has(word)) {
				this.showMessage(`'${word}' has already been used`, "err");
			} else {
				this.showMessage(`Added: ${word}`, "ok");
				this.score += word.length;
				this.showScore(this.score);
				this.words.add(word);
			}
		}

		$word.val("").focus();
	}

	async tick() {
		this.secs -= 1;
		this.showTimer();

		if (this.secs === 0) {
			clearInterval(this.timer);
			await this.scoreGame();
		}
	}

	async scoreGame() {
		$(".check-word", this.board).hide();
		$(".phrase", this.board).text("Congrats!");
		const resp = await axios.post("/final-score", { score: this.score });
		if (resp.data.brokeRecord) {
			this.showMessage(`New record: ${this.score}`, "ok");
		} else {
			this.showMessage(`Final score: ${this.score}`, "ok");
		}
	}
}

$(".restart").on("click", handleReset());

function handleReset() {
	game = new BoggleGame("boggle", 60);
}
