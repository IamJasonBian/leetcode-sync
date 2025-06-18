class FileSystem:
    def __init__(self):
        self.root = {'dirs': {}, 'files': {}}

    def _resolvePath(self, path: str):
        """Resolve a path to its directory node. Returns None if path doesn't exist."""
        if not path or path == '/':
            return self.root
            
        parts = [p for p in path.split('/') if p]
        current = self.root
        
        for part in parts:
            if part not in current['dirs']:
                return None
            current = current['dirs'][part]
        return current

    def ls(self, path: str) -> list[str]:
        """List directory contents or return file name if path points to a file."""
        if not path:
            return []
            
        # Handle root directory
        if path == '/':
            result = list(self.root['dirs'].keys()) + list(self.root['files'].keys())
            return sorted(result)
            
        # Handle file path
        if path in self.root['files']:
            return [path]
            
        # Handle directory path
        parts = [p for p in path.split('/') if p]
        current = self.root
        
        for i, part in enumerate(parts):
            if i == len(parts) - 1 and part in current['files']:
                return [part]
            if part not in current['dirs']:
                return []
            current = current['dirs'][part]
            
        # List directory contents
        result = list(current['dirs'].keys()) + list(current['files'].keys())
        return sorted(result)

    def mkdir(self, path: str) -> None:
        """Create a directory path. No-op if path already exists."""
        if not path or path == '/':
            return
            
        parts = [p for p in path.split('/') if p]
        current = self.root
        
        for part in parts:
            if part not in current['dirs']:
                current['dirs'][part] = {'dirs': {}, 'files': {}}
            current = current['dirs'][part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        """Add content to a file, creating it and its parent directories if needed."""
        if not filePath or filePath == '/':
            return
            
        # Split into directory path and filename
        parts = [p for p in filePath.split('/') if p]
        if not parts:
            return
            
        filename = parts[-1]
        dir_path = '/'.join(parts[:-1])
        
        # Create parent directories
        self.mkdir('/' + dir_path if dir_path else '')
        
        # Get parent directory
        parent = self._resolvePath('/' + dir_path) if dir_path else self.root
        if not parent:
            return
            
        # Add or update file
        if filename not in parent['files']:
            parent['files'][filename] = ''
        parent['files'][filename] += content

    def readContentFromFile(self, filePath: str) -> str:
        """Read content from a file. Returns empty string if file doesn't exist."""
        if not filePath or filePath == '/':
            return ''
            
        # Split into directory path and filename
        parts = [p for p in filePath.split('/') if p]
        if not parts:
            return ''
            
        filename = parts[-1]
        dir_path = '/'.join(parts[:-1])
        
        # Get parent directory
        parent = self._resolvePath('/' + dir_path) if dir_path else self.root
        if not parent or filename not in parent['files']:
            return ''
            
        return parent['files'][filename]
