<template>
    <BottomSheet
        @onClose="close"
        @onOpen="open"
        :data="{
            open: app.showFab,
            title: 'Add..',
        }"
    >
        <template #content>
            <section class="fab-content">
                <ul class="fab-content__list">
                    <li
                        v-for="(item, index) in fabConfig"
                        :key="index"
                        class="fab-content__element"
                    >
                        <div class="fab-content__image-container">
                            <IconBase
                                :data="{
                                    iconName: item.icon,
                                    iconColor: '#3F8CFF',
                                }"
                            />
                        </div>
                        <span class="fab-content__text">{{ item.text }}</span>
                    </li>
                </ul>
            </section>
        </template>
    </BottomSheet>
</template>

<script setup lang="ts">
import { BottomSheet } from '@/entities/bottom-sheet';
import { useAppModel } from '@/entities/app';
import { fabConfig } from '@/widgets/fab';
import { IconBase } from '@/shared/ui/icon-base';
import { lock, unlock } from '@/shared/lib/ustils/isBlockScroll';

const app = useAppModel();

const open = () => {
  lock();
};

const close = () => {
  app.updateShowFab(false);
  unlock();
};
</script>

<style scoped lang="scss">
  @import "style.module";
</style>
