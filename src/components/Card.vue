<template>
	<div class="card">
		<h3 id="text-h3">{{showDef? vocab.definition:vocab.word}}</h3>
		<b-button variant="outline-danger" size="sm" id="close-button" @click="$emit('remove-card', vocab.id)">Memorized</b-button>
		<b-button size="sm" id="toggle-def-button" @click="showDef = 1-showDef">{{showDef? "Hide definition" : "Show definition"}}</b-button>
	</div>
</template>

<script>
	export default {
		name: 'Card',
		props: ['vocab'],
		data() {
			return {
				showDef: false,
			}
		}
	}
</script>

<style scoped>
.card {
	width: 470px;
	min-height: 185px;
	display: flex;
	padding: $global_gap;
	border-radius: 5px;
	box-shadow: $shadow;
	background: #a7daf9;
	border: 4px ;
	margin: 20px auto;
	position: relative;
}

#text-h3 {
	text-align: center;
	margin: auto auto;
	padding: 10px 10px;
}

#close-button {
	position: absolute;
	top: 5px;
	left: 5px;
	height: 30px;
	width: 80px;
	font-size: 10px;
}

#toggle-def-button{
	position: absolute;
	bottom: 5px;
	right: 5px;
	height: 40px;
	width: 80px;
	font-size: 10px;
}
</style>