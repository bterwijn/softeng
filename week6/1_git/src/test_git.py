import pytest
import subprocess
import os

def run_git(repo_path, *args):
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git"] + list(args),
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr}"
    return result.stdout.strip()


def test_conflict_resolved():
    """Test that working_copy_1 had a conflict that was resolved."""
    repo_path = os.path.join(os.path.dirname(__file__), "working_copy_1")
    
    # Check that the repo exists
    assert os.path.isdir(repo_path), f"Repository not found at {repo_path}"
    
    # Find merge commits (commits with 2+ parents indicate a merge occurred)
    merge_commits = run_git(repo_path, "rev-list", "--merges", "--all").splitlines()
    assert len(merge_commits) > 0, "No merge commits found - no conflict could have occurred"
    
    # For each merge commit, check if both parents modified the same file
    # (this indicates a potential conflict that was resolved)
    conflict_was_resolved = False
    for merge_commit in merge_commits:
        # Get the two parent commits
        parents = run_git(repo_path, "rev-parse", f"{merge_commit}^1", f"{merge_commit}^2").splitlines()
        if len(parents) < 2:
            continue
        
        # Get files changed by each parent relative to merge base
        merge_base = run_git(repo_path, "merge-base", parents[0], parents[1])
        
        files_parent1 = set(run_git(repo_path, "diff", "--name-only", merge_base, parents[0]).splitlines())
        files_parent2 = set(run_git(repo_path, "diff", "--name-only", merge_base, parents[1]).splitlines())
        
        # If both parents modified the same file, there was likely a conflict
        common_files = files_parent1 & files_parent2
        if common_files:
            conflict_was_resolved = True
            break
    
    assert conflict_was_resolved, "No evidence of a resolved conflict (no merge with overlapping file changes)"
    
    # Verify no conflict markers remain in any tracked file
    tracked_files = run_git(repo_path, "ls-files").splitlines()
    for filename in tracked_files:
        file_path = os.path.join(repo_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                content = f.read()
            assert "<<<<<<<" not in content, f"Unresolved conflict markers found in {filename}"
            assert "=======" not in content, f"Unresolved conflict markers found in {filename}"
            assert ">>>>>>>" not in content, f"Unresolved conflict markers found in {filename}"

