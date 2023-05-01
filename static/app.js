class BoggleGame {
	constructor(boardId, secs = 60) {
		this.secs = secs;
		this.board = $("#" + boardId);
	}

	runme() {
		console.log(this.board);
		console.log(this.board.get(0));
	}
}
