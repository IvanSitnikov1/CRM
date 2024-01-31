<template>
  <teleport to="body">
    <transition name="pop-up">
      <aside class="pop-up"
             v-if="data.open"
             @click.self="closePopUp"
             ref="PupUpRef"
      >
          <section class="pop-up__content">
            <header class="pop-up__header" :class="{'pop-up__header_full': isReaching }">
              <img src="@/shared/assets/icons/close.svg"
                   alt="close"
                   class="pop-up__close"
                   @click="closePopUp"
              >
              <Title :data="{
                size: 'medium',
                title: data.title,
                isHighLeading: true
              }"/>
            </header>
            <main class="pop-up__main">
              <slot name="content">
              </slot>
            </main>
          </section>
      </aside>
    </transition>
  </teleport>
</template>

<script setup lang="ts">
import { Title } from '@/shared/ui/title'
import type { IPopUp } from '@/entities/popup'
import { useScroll } from '@vueuse/core'

const PupUpRef = ref<HTMLElement | null>(null)
const { y } = useScroll(PupUpRef)
const props = defineProps<{
  data: IPopUp
}>()

const isReaching = computed(() => y.value >= 134 )
const emit = defineEmits(['onClose'])

const closePopUp = () => {
  emit('onClose')
};
</script>

<style lang="scss">
 @import "style.module";
</style>
