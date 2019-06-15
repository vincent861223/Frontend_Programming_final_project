<template>
	<div id="flashCardView">
		<h1>Flashcards</h1>
		<CardStack :vocabulary="vocabulary"></CardStack>
	</div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
//import Card from '@/components/Card.vue'
import CardStack from '@/components/CardStack.vue'
import Vue from 'vue'

export default {
	name: 'flashCardView',
	components: {
		CardStack
	},
	props: ['vocabulary']
}
</script>
