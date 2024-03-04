<template>
  <teleport to="body">
    <transition name="bottom-sheet">
      <aside class="bottom-sheet" v-if="data.open" @click.self="closeBottomSheet">
          <section class="bottom-sheet__content"
                   :style="{ transform: 'translateY(' + y + 'px)' }"
                   @mousedown="handleDown"
                   @mousemove="handleMove"
                   @mouseleave="handleUp"
                   @mouseup="handleUp"
                   @touchmove="handleMove"
                   @touchstart="handleDown"
                   @touchend="handleUp"
          >
            <header class="bottom-sheet__header">
              <hr class="bottom-sheet__line">
              <Title :data="{
                size: 'medium',
                title: data.title,
                isHighLeading: true
              }"/>
            </header>
            <main class="bottom-sheet__content_overflow">
              <slot name="content">
              </slot>
            </main>
            <footer class="bottom-sheet__action">
              <slot name="actions">
              </slot>
            </footer>
          </section>
      </aside>
    </transition>
  </teleport>
</template>

<script setup lang="ts">
import { Title } from '@/shared/ui/title'
import type { IBottomSheet } from '@/entities/bottom-sheet'

const props = defineProps<{
  data: IBottomSheet
}>()

const emit = defineEmits(['onClose','onOpen'])

const y = ref(0);
const dragging = ref(false);
const startClientY = ref(0);

// Handle mouse move event
const handleDown = (event: MouseEvent | TouchEvent) => {
  dragging.value = true;
  startClientY.value = event instanceof MouseEvent ? event.clientY : event.touches[0].clientY;
};

const handleMove = (event: MouseEvent | TouchEvent) => {
  if (!dragging.value && !event instanceof TouchEvent) {
    return;
  }
  const clientY = event instanceof MouseEvent ? event.clientY : event.touches[0].clientY;
  const delta = Math.ceil(clientY - startClientY.value);
  y.value = delta > 0 ? delta : 0;
};

const handleUp = () => {
  dragging.value = false;
  if (y.value > window.innerHeight * 0.25) {
    emit('onClose')
  }
  y.value = 0
};
const closeBottomSheet = () => {
  emit('onClose')
};

watch(() => props.data.open, (value) => {
  if (value) {
    emit('onOpen')
  }
})
</script>

<style lang="scss">
 @import "style.module";
</style>
