# Test Specification

## CLI Tests (`apps/cli/tests/`)
1. **Add Task**: Verify tasks are added to the in-memory list with correct titles.
2. **Toggle Status**: Verify `toggle_task` switches `is_completed` correctly.
3. **Delete Task**: Verify tasks are removed from the list.

## API Tests (`apps/api/tests/`)
1. **Endpoint Health**: Verify `/api/v1/todos` returns 200 OK.
2. **CRUD Operations**:
    - Test POST creation.
    - Test GET fetching.
    - Test PATCH updating.
    - Test DELETE removal.
3. **Filtering**: Verify `search` query parameter correctly filters results.
