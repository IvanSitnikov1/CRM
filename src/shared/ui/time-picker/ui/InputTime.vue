<template>
    <UIInput
        @click="handlerOpenSelectTime"
        :data="{
            type: 'text',
            title: 'Time',
            placeholder: 'Select time',
            iconName: 'clock',
            isReadonly: true,
            name: 'task',
            value: '',
        }"
    />
    <BottomSheet
        :data="{
            title: 'Time',
            open: state.open,
        }"
        @onClose="close"
        @onOpen="open"
    >
        <template #content>
            <div class="date-selector">
                <TimePicker
                    :data="{
                        source: generateHours(),
                        count: 24,
                        value: state.hour,
                        sensitivity: 0.8,
                    }"
                    @onChange="setHours($event)"
                />
                <TimePicker
                    :data="{
                        source: generateMinutes(),
                        count: 20,
                        sensitivity: 0.8,
                        value: state.minutes,
                    }"
                    @onChange="setMinutes($event)"
                />
            </div>
        </template>
    </BottomSheet>
</template>

<script setup lang="ts">

import { TimePicker } from '@/shared/ui/time-picker';
import { BottomSheet } from '@/entities/bottom-sheet';
import { UIInput } from '@/shared/ui/input';
import { lock, unlock } from '@/shared/lib/ustils/isBlockScroll'

const state = reactive({
  open: false,
  hour: 0,
  minutes: 0
});

const setCurrentTime = () => {
  const now = new Date();
  state.hour = now.getHours();
  state.minutes = now.getMinutes();
};

const handlerOpenSelectTime = () => {
  state.open = true;
}

const setHours = (hour: number) => {
  state.hour = hour;
};

const setMinutes = (minutes: number) => {
  state.minutes = minutes;
};
const generateHours = () => new Array(24).fill(1).map((v, i) => ({ value: i, text: i }));

const generateMinutes = () => new Array(60).fill(1).map((v, i) => ({ value: i, text: i }));

const open = () => {
  lock();
};
const close = () => {
  state.open = false;
  unlock();
};

onMounted(() => setCurrentTime());
</script>
