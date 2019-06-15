<template>
	<div class="vocabulary-list">
		<b-button @click="removeSelected" id="remove-button">Remove</b-button>
		<b-button v-b-modal.modal-1 id="addVocab-button">Add vocabulary</b-button>
		  <b-modal id="modal-1" ref="modal" hide-footer title="Add vocabulary" @show='resetNewVocab'>
			<b-form @submit="addNewVocab" @reset="resetNewVocab" >
				<b-form-group id="word-form" label="Vocabulary:" label-for="word-input" description="Enter your new vocabulary">
					<b-form-input id="word-input" v-model="newVocab.word" type="text" required placeholder="Enter new vocabulary"></b-form-input>
					<b-form-input id="def-input" v-model="newVocab.definition" type="text" required placeholder="Enter definition for the new vocabulary"></b-form-input>
				</b-form-group>
				<b-button type="submit" variant="primary">Submit</b-button>
				<b-button type="reset" variant="danger">Reset</b-button>
			</b-form>
		  </b-modal>
		<section class="uk-container uk-section">
			<Datatable :titles="titles" :itemList="vocabulary" :search-attrs="searchAttr" @selected-change="addSelectedItems"></Datatable>
		</section>
	</div>
</template>

<script>
	import Vue from 'vue'
	import Datatable from 'vue-uikit-datatable'
	import 'uikit/dist/css/uikit.min.css'

	Vue.use(Datatable)
	export default {
		name: 'vocabularyList',
		components: {

		},
		props: ['vocabulary'],
		data (){
			return {
				titles: [
				{
					prop: "word",
					name: "Word"
				},
				{
					prop: "definition",
					name: "Definition"
				}
				],
				searchAttr: ["word", "definition"],
				selectedItems: [],
				newVocab: {
					id: 0,
					word: "",
					definition: ""
				}
			}
		},
		methods: {
			addSelectedItems: function(items) {
				this.selectedItems = items;
			},
			removeSelected: function(){
				for(var i = 0; i < this.selectedItems.length; i++){
					for(var j = 0; j < this.vocabulary.length; j++){
						if(this.vocabulary[j].id == this.selectedItems[i].id){
							this.vocabulary.splice(j, 1);
							break;
						}
					}
				}
			},
			addNewVocab: function(e){
				//console.log(this.newVocab)
				//var newVocab = Object.assign({}, this.newVocab);
				//this.vocabulary = Object.assign({}, this.vocabulary, this.newVocab)
				e.preventDefault();
				this.vocabulary.unshift({id: this.newVocab.id, word: this.newVocab.word, definition: this.newVocab.definition})
				this.resetNewVocab();
				this.$nextTick(() => { this.$refs.modal.hide() });
				return;
			},
			resetNewVocab: function() {
				this.newVocab.id = -1;
				this.newVocab.word = "";
				this.newVocab.definition = "";
			}
		}
	}
</script>


<style scoped>

#remove-button{
	margin: 0px 20px;
}
#addVocab-button{
	margin: 0px 20px;
}

</style>

