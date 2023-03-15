import pytest
import asyncio
from unittest.mock import Mock
from patterns.behavioural.observer.python.pattern import EventEmitter
from patterns.behavioural.command.python.pattern import TextEditor, InsertCommand, CommandInvoker
from patterns.behavioural.strategy.python.pattern import Sorter, BubbleSort, QuickSort

@pytest.mark.asyncio
async def test_observer_invariant():
    emitter = EventEmitter()
    callback = Mock()
    emitter.on("event", callback)
    
    await emitter.emit("event", "data")
    callback.assert_called_once_with("data")

def test_command_undo_restores_state():
    editor = TextEditor()
    invoker = CommandInvoker()
    
    invoker.execute_command(InsertCommand(editor, "A"))
    assert editor.get_text() == "A"
    
    invoker.execute_command(InsertCommand(editor, "B"))
    assert editor.get_text() == "AB"
    
    invoker.undo()
    assert editor.get_text() == "A"

def test_strategy_switching():
    data = [5, 2, 8]
    sorter = Sorter(BubbleSort())
    assert sorter.sort_data(data) == [2, 5, 8]
    
    sorter.set_strategy(QuickSort())
    assert sorter.sort_data(data) == [2, 5, 8]
