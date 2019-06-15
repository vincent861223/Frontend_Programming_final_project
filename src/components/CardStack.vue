<template>
	<div class="cardStack">
		<b-button @click="shuffledVocab()">Shuffle</b-button>
		<Card v-for="(vocab, index) in vocabulary_" :key="vocab.id" :vocab="vocab" @remove-card="removeCard"></Card>
	</div>
</template>

<script>
import Card from './Card.vue'
import Vue from 'vue'
export default{
	name: 'CardStack',
	components: {
		Card
	},
	props: ['vocabulary'],
	data() {
		return {
			vocabulary_: [...this.vocabulary]
		}
	},
	methods: {
		removeCard: function(index){
			for(var i = 0; i < this.vocabulary_.length; i++){
				if(this.vocabulary_[i].id == index) this.vocabulary_.splice(i, 1)
			}
		},
		shuffledVocab: function(){
			console.log('shuffledVocab')
			//console.log(typeof(this.vocabulary_))
			for(var i = this.vocabulary_.length-1; i > 0; i--){
				var j = Math.floor(Math.random() * (i + 1));
				console.log(this.vocabulary_[i])
				var tmp = this.vocabulary_[i];
				Vue.set(this.vocabulary_, i, this.vocabulary_[j])
				Vue.set(this.vocabulary_, j, tmp)
			}
		}
	}
}
</script>

